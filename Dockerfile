# ==========================================
# Stage 1: Build Binary
# ==========================================
FROM golang:1.23-alpine AS builder

RUN apk add --no-cache git build-base ca-certificates

WORKDIR /app

# Copy all repository files into the container
COPY . .

# Initialize the module if missing
RUN if [ ! -f go.mod ]; then \
        go mod init credkellar/frequency && \
        go mod tidy; \
    else \
        go mod tidy; \
    fi

# FIX: Changed the trailing "." to "./..." so Go searches all subfolders for your main.go
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o frequency ./...

# ==========================================
# Stage 2: Minimal Runtime
# ==========================================
FROM alpine:3.19 AS runner

RUN apk add --no-cache ca-certificates tzdata

WORKDIR /app

# Copy the compiled binary over
COPY --from=builder /app/frequency .

ENTRYPOINT ["./frequency"]
